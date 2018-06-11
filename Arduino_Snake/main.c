// Display needs it!
#include <Arduino.h>
#include <LiquidCrystal.h>
#include <EEPROM.h>

// Matrix Board
#define LEDARRAY_D 13
#define LEDARRAY_C 12
#define LEDARRAY_B 11
#define LEDARRAY_A 10
#define LEDARRAY_G 9
#define LEDARRAY_DI 8
#define LEDARRAY_CLK 7
#define LEDARRAY_LAT 6

// LCD
#define RS A3
#define EN A2
#define D4 0
#define D5 1
#define D6 2
#define D7 3

// Stuff
#define SWITCH 5
#define BUZZER 4

// Potentiometers
#define UP_DOWN A4
#define LEFT_RIGHT A5

LiquidCrystal lcd(RS, EN, D4, D5, D6, D7);

// Some stuff display writing needs.
unsigned char Display_Buffer[2];
unsigned int Word1[32];

// Snake
int snake[200][2] = {{7, 7}};   // Complete snake location.
int current[2] = {7, 7};        // Front of snake location. (Temporary)
int food[2] = {2, 4};           // Food location.
int dir = 0;                    // Direction snake heading in. (0 up, 1 right, 2 down, 3 left)
int up_down = 0;                // Left and right direction for stick.
int left_right = 0;             // Up and down direction for stick.
int count = 1;                  // Current snake length.
int death_sec = 500;            // Seconds for each snake part removal.
int btn = 1;                    // Temporary value to ensure not holding button.
int speed = 200;                // Game speed, in ms.
int highscore = 0;              // Highscore this session.
int score = 0;                  // Score so that I can update highscore.

bool dead = false;              // Player dead?
bool play = false;              // Playing?
bool began = false;             // Has the user started yet?

unsigned long previousMillis = 0;
unsigned long previousMillis2 = 0;

// First menu screen, startup screen. (Turning on all LEDs to ensure no dead LEDs)
char Scene[16][16] = {
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
};

// Setup for pins and serial.
void setup() {
    // Display pins.
    pinMode(LEDARRAY_D, OUTPUT);
    pinMode(LEDARRAY_C, OUTPUT);
    pinMode(LEDARRAY_B, OUTPUT);
    pinMode(LEDARRAY_A, OUTPUT);
    pinMode(LEDARRAY_G, OUTPUT);
    pinMode(LEDARRAY_DI, OUTPUT);
    pinMode(LEDARRAY_CLK, OUTPUT);
    pinMode(LEDARRAY_LAT, OUTPUT);

    // LCD Screen Pins
    pinMode(RS, OUTPUT);
    pinMode(EN, OUTPUT);
    pinMode(D4, OUTPUT);
    pinMode(D5, OUTPUT);
    pinMode(D6, OUTPUT);
    pinMode(D7, OUTPUT);

    pinMode(SWITCH, INPUT); // Switch pin.
    pinMode(BUZZER, OUTPUT); // Buzzer.

    digitalWrite(SWITCH, HIGH); // Required to get switch started.

    // Welcome to snake!
    lcd.begin(16, 2);
    lcd.print("The Snake!");
    lcd.setCursor(0, 1);
    lcd.print("Click to Start.");

    EEPROM.get(0, highscore); // Get the highscore
    highscore -= 256; // Adds 256 for some reason.
}

// Game loop to run every frame.
void Game() {
    unsigned long currentMillis = millis(); // Set current seconds.

    if (play) { // Is user playing?
        if (dead) { // Is user dead?
            // If they are dead begin removing snake parts.
            if (currentMillis - previousMillis >= death_sec) { // After seconds to remove next part?
                previousMillis = currentMillis; // Set the previous seconds to now.
                death_sec /= 1.1; // Reduce time for next one, don't want to take all day.
                renderDeath(); // Call the render function to render death.
            }
        } else { // They are playing.
            // Only move the pieces every 
            if (currentMillis - previousMillis >= speed) { // Follow game speed.
                previousMillis = currentMillis; // Set the previous seconds to now.
                moveSnake(); // Call the moving snake functions.
            }
        }

        // Direction and render checkings should not follow the delays.
        if (currentMillis - previousMillis2 >= 50) { // Follow game speed.
                previousMillis2 = currentMillis; // Set the previous seconds to now.
            checkDirection();
        }
        render();
    }

    // Check if the switch doesn't match old value.
    if (digitalRead(SWITCH) != btn) { // Protects against holding the button, toggle mode.
        btn = digitalRead(SWITCH); // Set old value to the one now.
        if (btn == 0) {
            play = !play; // If the button is pressed, set play mode to whatever it wasn't.
            if (play)
                updateLCDScore(false); // Have it display the score again.
            else {
                // Update to show the game is paused.
                lcd.clear();
                lcd.setCursor(0, 0);
                lcd.print("Paused...");
                lcd.setCursor(0, 1);
                lcd.print("Press to Resume.");
            }
        }
    }

}

// Check the direction of the joystick.
void checkDirection() {
    up_down = analogRead(UP_DOWN); // Get the up and down potentiometer.
    left_right = analogRead(LEFT_RIGHT); // Get the left and right potentiometer.
    if (up_down > 920) { // Down?
        if (dir != 0) // Make sure they are not going into themselves.
            dir = 2; 
    } else if (up_down < 320) { // Up?
        if (dir != 2)
            dir = 0;
    } else if (left_right > 920) { // Left?
        if (dir != 1)
            dir = 3;
    } else if (left_right < 320) { // Right?
        if (dir != 3)
            dir = 1;
    }
}

// Move the snake
void moveSnake() {
    // Based on direction move the snake in the direction
    if (dir == 0)
        current[0]--;
    else if (dir == 1)
        current[1]++;
    else if (dir == 2)
        current[0]++;
    else if (dir == 3)
        current[1]--;

    // If the user hits a wall, they are dead.
    if (current[1] > 15 || current[1] < 0 || current[0] > 15 || current[0] < 0) {
        // Tell em how they died
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("BOOM!");
        lcd.setCursor(0, 1);
        lcd.print("Press to Restart!");
        dead = true; // Dead
        score = count; // Set the score to length.
        return; // Return the function not continue.
    }

    // Add the current values to the snakes length.
    snake[count][0] = current[0];
    snake[count][1] = current[1];

    // Eaten food
    if (food[0] == current[0] && food[1] == current[1]) {
        tone(BUZZER, 1000, 100); // Play the buzzer
        // Generate a new food particle.
        safeFoodSpawn();

        count++; // Increase length of snake.
        speed *= 0.99; // Increase the speed of the game by 1%.
        updateLCDScore(true); // Update score on LCD.
    } else
        removeFirstValue(true); // Remove the last part of the snake to move.

}

// Render snake
void render() {
    clearScene(); // Clear the last frame
    // Go through and render each part of the snake.
    for (int i = 0; i < count; i++)
        Scene[snake[i][0]][snake[i][1]] = 0;
    Scene[food[0]][food[1]] = 0; // Render the snake.
}

// Remove the last part of the snake.
void removeFirstValue(bool checking) {
    // Go through the whole snake and move all the values down.
    for (int i = 0; i < count; i++) {
        // Do this when dead, don't want to waste time seeing if it touches.
        if (checking) {
            if (current[0] == snake[i][0] && current[1] == snake[i][1]) {
                // Tell em how they died
                lcd.clear();
                lcd.setCursor(0, 0);
                lcd.print("OOF!");
                lcd.setCursor(0, 1);
                lcd.print("Press to Restart!");
                dead = true; // Snake touches itself, dead
                score = count; // Set the score to length.
            }

            // Move each part of the array down.
            snake[i][0] = snake[i + 1][0];
            snake[i][1] = snake[i + 1][1];
        }
    }
}

// Player is dead
void renderDeath() {
    // Is it down to 1 part left?
    if (count > 1) { // If not
        removeFirstValue(false); // Remove the part
        count--; // Reduce the length count.
        tone(BUZZER, 1000, death_sec / 1.25); // Play the death buzzer
    } else {
        // Beaten highscore?
        if (highscore < score) {
            highscore = score; // Store new highscore.
            updateLCDScore(false); // Reset LCD to new highscore.
            EEPROM.write(0, highscore); // Write the new highscore to memory.
            // YOU WON.
            lcd.clear();
            lcd.setCursor(0, 0);
            lcd.print("Winner Winner!");
            lcd.setCursor(0, 1);
            lcd.print("New Highscore!");
        }
        
        // Reset all the values of the player.
        dead = false;
        play = false;
        current[0] = 7; // Put them back in the middle.
        current[1] = 7;
        snake[0][0] = current[0]; // Update the snake value.
        snake[0][1] = current[1];
        count = 1;
        death_sec = 500;
        dir = 0; // Direction back up.
        began = false;
        speed = 200;
    }
}

void updateLCDScore(bool update) {
    if (update) {
        // Only update the score.
        // Clearing causes a bit of lag.
        lcd.setCursor(7, 0);
        lcd.print(String(count));
    } else {
        // Clear when the pause shows up.
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Score: " + String(count));
        lcd.setCursor(0, 1);
        lcd.print("Highscore: " + String(highscore));
    }
}

// Find a safe spawn for food.
void safeFoodSpawn() {
    bool found = false; // Found that they conflict with snake.

    // Generate random location.
    food[0] = random(16);
    food[1] = random(16);

    // Search to see if the food conflicts with the snake.
    for (int i = 0; i < count; i++) {
        if (snake[i][0] == food[0] && snake[i][1] == food[1]) {
            found = true; // Found a conflict
            break; // Ditch the loop
        }
    }

    // If found, restart. the food check.
    if (found)
        safeFoodSpawn();
}

// Screen Rendering Functions - Mine
// --------------------------------------------------------

// Clear the current frame.
void clearScene() {
    int a, b = 0;
    for (a = 0; a < 16; a++) {
        for (b = 0; b < 16; b++)
            Scene[a][b] = 1;
    }
}

// Screen Rendering Functions - Not mine
// --------------------------------------------------------
void SceneToWord() {
    int i, k, key = 0;
    unsigned int value;
    for (i = 0; i < 16; i++) {
        for (k = 0; k < 16; k++) {
            if (i < 8) {
                value = Scene[i][k] << (7 - i);
                Word1[15 - k] += value;
            } else {
                value = Scene[i][k] << (15 - i);
                Word1[31 - k] += value;
            }
        }
    }
}

void Display(unsigned int dat[]) {
    unsigned char i;

    for (i = 0; i < 16; i++) {
        digitalWrite(LEDARRAY_G, HIGH);

        Display_Buffer[0] = dat[i];
        Display_Buffer[1] = dat[i + 16];

        Send(Display_Buffer[1]);
        Send(Display_Buffer[0]);

        digitalWrite(LEDARRAY_LAT, HIGH);
        delayMicroseconds(1);

        digitalWrite(LEDARRAY_LAT, LOW);
        delayMicroseconds(1);

        Scan_Line(i);

        digitalWrite(LEDARRAY_G, LOW);

        delayMicroseconds(100);
    }
}

void Scan_Line(unsigned int m) {
    switch (m) {
    case 0:
        digitalWrite(LEDARRAY_D, LOW);
        digitalWrite(LEDARRAY_C, LOW);
        digitalWrite(LEDARRAY_B, LOW);
        digitalWrite(LEDARRAY_A, LOW);
        break;
    case 1:
        digitalWrite(LEDARRAY_D, LOW);
        digitalWrite(LEDARRAY_C, LOW);
        digitalWrite(LEDARRAY_B, LOW);
        digitalWrite(LEDARRAY_A, HIGH);
        break;
    case 2:
        digitalWrite(LEDARRAY_D, LOW);
        digitalWrite(LEDARRAY_C, LOW);
        digitalWrite(LEDARRAY_B, HIGH);
        digitalWrite(LEDARRAY_A, LOW);
        break;
    case 3:
        digitalWrite(LEDARRAY_D, LOW);
        digitalWrite(LEDARRAY_C, LOW);
        digitalWrite(LEDARRAY_B, HIGH);
        digitalWrite(LEDARRAY_A, HIGH);
        break;
    case 4:
        digitalWrite(LEDARRAY_D, LOW);
        digitalWrite(LEDARRAY_C, HIGH);
        digitalWrite(LEDARRAY_B, LOW);
        digitalWrite(LEDARRAY_A, LOW);
        break;
    case 5:
        digitalWrite(LEDARRAY_D, LOW);
        digitalWrite(LEDARRAY_C, HIGH);
        digitalWrite(LEDARRAY_B, LOW);
        digitalWrite(LEDARRAY_A, HIGH);
        break;
    case 6:
        digitalWrite(LEDARRAY_D, LOW);
        digitalWrite(LEDARRAY_C, HIGH);
        digitalWrite(LEDARRAY_B, HIGH);
        digitalWrite(LEDARRAY_A, LOW);
        break;
    case 7:
        digitalWrite(LEDARRAY_D, LOW);
        digitalWrite(LEDARRAY_C, HIGH);
        digitalWrite(LEDARRAY_B, HIGH);
        digitalWrite(LEDARRAY_A, HIGH);
        break;
    case 8:
        digitalWrite(LEDARRAY_D, HIGH);
        digitalWrite(LEDARRAY_C, LOW);
        digitalWrite(LEDARRAY_B, LOW);
        digitalWrite(LEDARRAY_A, LOW);
        break;
    case 9:
        digitalWrite(LEDARRAY_D, HIGH);
        digitalWrite(LEDARRAY_C, LOW);
        digitalWrite(LEDARRAY_B, LOW);
        digitalWrite(LEDARRAY_A, HIGH);
        break;
    case 10:
        digitalWrite(LEDARRAY_D, HIGH);
        digitalWrite(LEDARRAY_C, LOW);
        digitalWrite(LEDARRAY_B, HIGH);
        digitalWrite(LEDARRAY_A, LOW);
        break;
    case 11:
        digitalWrite(LEDARRAY_D, HIGH);
        digitalWrite(LEDARRAY_C, LOW);
        digitalWrite(LEDARRAY_B, HIGH);
        digitalWrite(LEDARRAY_A, HIGH);
        break;
    case 12:
        digitalWrite(LEDARRAY_D, HIGH);
        digitalWrite(LEDARRAY_C, HIGH);
        digitalWrite(LEDARRAY_B, LOW);
        digitalWrite(LEDARRAY_A, LOW);
        break;
    case 13:
        digitalWrite(LEDARRAY_D, HIGH);
        digitalWrite(LEDARRAY_C, HIGH);
        digitalWrite(LEDARRAY_B, LOW);
        digitalWrite(LEDARRAY_A, HIGH);
        break;
    case 14:
        digitalWrite(LEDARRAY_D, HIGH);
        digitalWrite(LEDARRAY_C, HIGH);
        digitalWrite(LEDARRAY_B, HIGH);
        digitalWrite(LEDARRAY_A, LOW);
        break;
    case 15:
        digitalWrite(LEDARRAY_D, HIGH);
        digitalWrite(LEDARRAY_C, HIGH);
        digitalWrite(LEDARRAY_B, HIGH);
        digitalWrite(LEDARRAY_A, HIGH);
        break;
    default:
        break;
    }
}

void Send(unsigned int dat) {
    unsigned char i;
    digitalWrite(LEDARRAY_CLK, LOW);
    delayMicroseconds(1);;
    digitalWrite(LEDARRAY_LAT, LOW);
    delayMicroseconds(1);;

    for (i = 0; i < 8; i++) {
        if (dat & 0x01) {
            digitalWrite(LEDARRAY_DI, HIGH);
        } else {
            digitalWrite(LEDARRAY_DI, LOW);
        }

        delayMicroseconds(1);
        digitalWrite(LEDARRAY_CLK, HIGH);
        delayMicroseconds(1);
        digitalWrite(LEDARRAY_CLK, LOW);
        delayMicroseconds(1);
        dat >>= 1;

    }
}

void update() {
    clearWord();
    SceneToWord();
}

void clearWord() {
    for (int i = 0; i < 32; i++)
        Word1[i] = 0;
}

void loop() {
    Game();
    update();
    Display(Word1);
}