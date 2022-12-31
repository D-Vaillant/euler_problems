/* problem004.js
Finding a palindromic number.
*/

function solver() {
    var current_max = (91, 99);
    var bigpal = 91*99;

    for (var a = 999; a >= 800; a--) { // Cut it off at 800 because it's probably not worse.
        for (var b = 999; b >= a; b--) {
            var cand = a*b;
            if (isPalindrome(cand) && cand > bigpal) {
                current_max = (a, b);
                bigpal = a*b;
            }
        }
    }

    return bigpal;
}

function isPalindrome(num) {
    var numstr = String(num);  // lotta ways to do this
    var revstr = numstr.split('').reverse().join('')
    return numstr === revstr;
}

console.log(solver())