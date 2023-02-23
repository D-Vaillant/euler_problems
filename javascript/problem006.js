/* problem006.js
Sum square difference. 
Find the difference between (sum[1..100])**2
and sum[1**2 .. 100**2].
*/

var sum_of_first = 101 * 50;  // Thanks Gauss.
var square_sum = sum_of_first**2;

var sum_square = 0;
for (var i = 1; i <= 100; i++) {
    sum_square += i**2;
}

console.log(square_sum - sum_square);