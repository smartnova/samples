import $ from 'jquery';
import additionCalculator from './modules/addition-calculator';
import taxCalculator      from './modules/tax-calculator';

var item1Price = 400,
    item2Price = 600,
    totalPrice = additionCalculator(item1Price, item2Price),
    tax = 1.08,
    priceIncludeTax = taxCalculator(totalPrice, tax);

console.log(priceIncludeTax);
$('body').html(priceIncludeTax);
