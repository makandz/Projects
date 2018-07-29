// CQRT - Faster Square Roots, in a small file.
module.exports = class cqrt {
    constructor() {
        this.a = [];
        this.init();
    }
    init() {
        for (i = 0; i < 1E6; i++)
            this.a.push(Math.sqrt(i));
    }
    sqrt(b) {
        if (b >= 1E6) return Math.sqrt(~~b);
        else return this.a[~~b];
    }
}
