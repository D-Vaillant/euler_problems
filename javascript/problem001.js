// problem001.js
//  Find the sum of all multiples of 3 or 5 below 1000.

function algebraic(upper, factor) {
    upper = Math.floor((upper - 1) / factor);
    sum = (1+upper) * (upper/2)
    return Math.floor(factor * sum)
}

function main(maximum) {
    return algebraic(maximum, 3) + algebraic(maximum, 5) - algebraic(maximum, 15)
}

console.log(main(1000))
