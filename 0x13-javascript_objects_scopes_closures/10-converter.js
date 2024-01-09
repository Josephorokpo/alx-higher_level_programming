#!/usr/bin/node

exports.converter = function (base) {
  // Use a self-invoking function to avoid declaring new variables
  (function convert(num) {
    // If num is greater than or equal to base, continue converting
    num >= base && convert((num - num % base) / base);

    // Output the remainder after division as the converted value
    process.stdout.write(num % base < 10 ? num % base + '' : String.fromCharCode(num % base - 10 + 'a'.charCodeAt(0)));
  });
  process.stdout.write('\n'); // Print a new line after conversion
};
