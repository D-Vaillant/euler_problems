// problem002.js
// Fibonacci time!!

function fibonacci(num) {
    if (fibonacci.cache[num] == null) {
        fibonacci.cache[num] = fibonacci.cache[num-2] + fibonacci.cache[num-1];
    }
    return fibonacci.cache[num];
}

fibonacci.cache = {0: 1, 1: 1};

function main(max_value) {
    var i = 0;
    var out = 0;
    while (true) {
        var fib_i = fibonacci(i);
        if (fib_i > max_value) {
            break;
        } else if (fib_i %2 === 0) {
            out += fib_i;
        }
        i += 1;
    }
    return out;
}

console.log(main(4000000));

