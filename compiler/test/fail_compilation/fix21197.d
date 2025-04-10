// REQUIRED_ARGS: -c
// ERROR: 3: no property `front` for type `int[]`

void main() {
    alias T = typeof((int[]).front);
}