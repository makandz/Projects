#include <FrequencyTimer2.h>

// Pin Numbers
int anodes[] = {4, 5, 3};
int cathodes[] = {10, 8, 9};
int button = 2;

// Frame counting
int frame = 0;

// Button
int prevButton = 0;
int buttonTime = 0;

// Animation
int animation = 0; // Current animation (0: Moving bar)
int prevTime = 0; // Previous tick time.
int curTime = 0; // Current time.
int curTick = 0; // Current animation count.
bool changed = true; // Is the animation tick changed?

// Snake
bool growing = true;

// {0: off, 1: on}
int grid[3][3] = { // Matrix runs off this
    {0, 0, 0},
    {0, 0, 0},
    {0, 0, 0}
};

// Spinning animation (custom)
int spinner_animation[2][3][3] = {
    {
        {1, 0, 1},
        {0, 1, 0},
        {1, 0, 1}
    }, {
        {0, 1, 0},
        {1, 1, 1},
        {0, 1, 0}
    }
};

// Perimeter animation (custom)
int perimeter_animation[8][2] = {
    {0, 0},
    {0, 1},
    {0, 2},
    {1, 2},
    {2, 2},
    {2, 1},
    {2, 0},
    {1, 0},
};

// Snake animation (custom)
int snake_animation[9][2] = {
    {0, 0},
    {0, 1},
    {0, 2},
    {1, 2},
    {2, 2},
    {2, 1},
    {2, 0},
    {1, 0},
    {1, 1}
};

// Spinning animation (custom)
int swiping_animation[5][3][3] = {
    {
        {1, 0, 0},
        {0, 0, 0},
        {0, 0, 0}
    }, {
        {0, 1, 0},
        {1, 0, 0},
        {0, 0, 0}
    }, {
        {0, 0, 1},
        {0, 1, 0},
        {1, 0, 0}
    }, {
        {0, 0, 0},
        {0, 0, 1},
        {0, 1, 0}
    }, {
        {0, 0, 0},
        {0, 0, 0},
        {0, 0, 1}
    }
};

void setup() {
    Serial.begin(9600); // debugging

    // Int for button
    attachInterrupt(0, onButton, FALLING);

    // Set all pins to output state.
    for (int i = 0; i < 3; i++) {
        pinMode(anodes[i], OUTPUT);
        pinMode(cathodes[i], OUTPUT);
    }

    // Button pin
    pinMode(button, INPUT);

    // Turn off toggling of pin 11
    FrequencyTimer2::disable();
    // Set refresh rate (interrupt timeout period)
    FrequencyTimer2::setPeriod(32000);
    // Set interrupt routine to be called
    FrequencyTimer2::setOnOverflow(render);
}

void offGrid() {
    for (int i = 0; i < 3; i++) {
        for (int x = 0; x < 3; x++)
            grid[i][x] = 0;
    }
}

void render() {
    frame++;
    if (frame >= 3000) {
        animate();
        frame = 0;
    }

    // Loop through grid, state of LEDs.
    for (int i = 0; i < 3; i++) {
        digitalWrite(anodes[i], HIGH); // Turn on row
        for (int x = 0; x < 3; x++) {
            // Check for each LED.
            if (grid[i][x])
                digitalWrite(cathodes[x], LOW); // Turn on LED.
            digitalWrite(cathodes[x], HIGH); // TUrn off LED.
        }
        digitalWrite(anodes[i], LOW); // Turn off row.
    }
}

void animate() {
    // Moving bar
    if (animation == 0) {
        // Only three animations.
        if (curTick == 2) curTick = 0;
        else curTick++;

        // Change animation.
        offGrid();
        for (int i = 0; i < 3; i++) {
            for (int x = 0; x < 3; x++) {
                if (curTick == i) 
                    grid[i][x] = 1;
            }
        }

    // Spinner
    } else if (animation == 1) {
        // Only two animations.
        if (curTick == 1) curTick = 0;
        else curTick++;

        for (int i = 0; i < 3; i++) {
            for (int x = 0; x < 3; x++)
                grid[i][x] = spinner_animation[curTick][i][x];
        }

    // Perimeter
    } else if (animation == 2) {
        // Only two animations.
        if (curTick == 7) curTick = 0;
        else curTick++;

        // Turn all the LEDs on.
        for (int i = 0; i < 3; i++) {
            for (int x = 0; x < 3; x++) {
                grid[i][x] = 1;
            }
        }

        grid[perimeter_animation[curTick][0]][perimeter_animation[curTick][1]] = 0;
    
    // Snake
    } else if (animation == 3) {
        // Is the snake growing?
        if (growing) {
            grid[snake_animation[curTick][0]][snake_animation[curTick][1]] = 1;
            if (curTick == 8) growing = false;
            else curTick++;
            
        } else {
            grid[snake_animation[curTick][0]][snake_animation[curTick][1]] = 0;
            if (curTick == 0) growing = true;
            else curTick--;
        }
    
    // Swiping
    } else if (animation == 4) {
        // Only five animations.
        if (curTick == 4) curTick = 0;
        else curTick++;

        for (int i = 0; i < 3; i++) {
            for (int x = 0; x < 3; x++)
                grid[i][x] = swiping_animation[curTick][i][x];
        }
    }
}

void loop() {
    render(); // Grid Rendering
}

void onButton() {
    buttonTime = millis();

    // We've got 3 animations.
    if (buttonTime - prevButton > 250) {
        if (animation == 4)
            animation = 0;
        else animation++;
        offGrid(); // Reset grid
        curTick = 0; // Reset current timer.
        prevButton = buttonTime; // Set button time
    }
}
