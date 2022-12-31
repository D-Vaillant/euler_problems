/* problem003.js
What is the largest prime factor of the numer 600851475143?
*/
const number = 600851475143

function main(num) {
	top = Math.sqrt(num);  // because of math
	var lastFactor = 0;
	if (num % 2 === 0) {  // special case for i=2 so I can ignore all evens
		lastFactor = 2;
		num /= 2;
		while (num % 2 === 0) {
			num /= 2;
		}
	}
	var i = 3;
	while (num > 1 && lastFactor <= top) {
		if (num % i == 0) {
			if (num % i == 0) {
				lastFactor = i;
				num /= i;
				while (num % i === 0) {
					num /= i;
				}
			}
		}
		i += 2;  // because it's only odds
	}
	return lastFactor;
}

console.log(main(number));