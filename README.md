# num2eng
Convert integers (0 to 10^123-1 inclusive) to English and back

Just a little exercise/experiment c^:

```python
>>> import num2eng

>>> num2eng.int2eng(123)
'one hundred and twenty-three'

>>> num2eng.eng2int('one hundred and twenty-three')
123

>>> num2eng.int2eng(10**123-1)
'nine hundred and ninety-nine novemtrigintillion, nine hundred and ninety-nine octotrigintillion, nine hundred and ninety-nine septentrigintillion, nine hundred and ninety-nine sextrigintillion, nine hundred and ninety-nine quintrigintillion, nine hundred and ninety-nine quattuortrigintillion, nine hundred and ninety-nine tretrigintillion, nine hundred and ninety-nine duotrigintillion, nine hundred and ninety-nine untrigintillion, nine hundred and ninety-nine trigintillion, nine hundred and ninety-nine novemvigintillion, nine hundred and ninety-nine octovigintillion, nine hundred and ninety-nine septenvigintillion, nine hundred and ninety-nine sexvigintillion, nine hundred and ninety-nine quinvigintillion, nine hundred and ninety-nine quattuorvigintillion, nine hundred and ninety-nine trevigintillion, nine hundred and ninety-nine duovigintillion, nine hundred and ninety-nine unvigintillion, nine hundred and ninety-nine vigintillion, nine hundred and ninety-nine novemdecillion, nine hundred and ninety-nine octodecillion, nine hundred and ninety-nine septendecillion, nine hundred and ninety-nine sexdecillion, nine hundred and ninety-nine quindecillion, nine hundred and ninety-nine quattuordecillion, nine hundred and ninety-nine tredecillion, nine hundred and ninety-nine duodecillion, nine hundred and ninety-nine undecillion, nine hundred and ninety-nine decillion, nine hundred and ninety-nine nonillion, nine hundred and ninety-nine octillion, nine hundred and ninety-nine septillion, nine hundred and ninety-nine sextillion, nine hundred and ninety-nine quintillion, nine hundred and ninety-nine quadrillion, nine hundred and ninety-nine trillion, nine hundred and ninety-nine billion, nine hundred and ninety-nine million, nine hundred and ninety-nine thousand, nine hundred and ninety-nine'

>>> num2eng.eng2int('nine hundred and ninety-nine novemtrigintillion, nine hundred and ninety-nine octotrigintillion, nine hundred and ninety-nine septentrigintillion, nine hundred and ninety-nine sextrigintillion, nine hundred and ninety-nine quintrigintillion, nine hundred and ninety-nine quattuortrigintillion, nine hundred and ninety-nine tretrigintillion, nine hundred and ninety-nine duotrigintillion, nine hundred and ninety-nine untrigintillion, nine hundred and ninety-nine trigintillion, nine hundred and ninety-nine novemvigintillion, nine hundred and ninety-nine octovigintillion, nine hundred and ninety-nine septenvigintillion, nine hundred and ninety-nine sexvigintillion, nine hundred and ninety-nine quinvigintillion, nine hundred and ninety-nine quattuorvigintillion, nine hundred and ninety-nine trevigintillion, nine hundred and ninety-nine duovigintillion, nine hundred and ninety-nine unvigintillion, nine hundred and ninety-nine vigintillion, nine hundred and ninety-nine novemdecillion, nine hundred and ninety-nine octodecillion, nine hundred and ninety-nine septendecillion, nine hundred and ninety-nine sexdecillion, nine hundred and ninety-nine quindecillion, nine hundred and ninety-nine quattuordecillion, nine hundred and ninety-nine tredecillion, nine hundred and ninety-nine duodecillion, nine hundred and ninety-nine undecillion, nine hundred and ninety-nine decillion, nine hundred and ninety-nine nonillion, nine hundred and ninety-nine octillion, nine hundred and ninety-nine septillion, nine hundred and ninety-nine sextillion, nine hundred and ninety-nine quintillion, nine hundred and ninety-nine quadrillion, nine hundred and ninety-nine trillion, nine hundred and ninety-nine billion, nine hundred and ninety-nine million, nine hundred and ninety-nine thousand, nine hundred and ninety-nine')
999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999

>>> num2eng.int2eng(123, True)  # ordinal numbers
'one hundred and twenty-third'

>>> num2eng.eng2int('one hundred and twenty-third')  # and back
123

>>> num2eng.nth(1)  # nth numbers
'1st'

>>> num2eng.nth(11)  # english is weird
'11th'

>>> num2eng.nth(21)  # what
'21st'

>>> num2eng.card2ord("one")
'first'

>>> num2eng.ord2card("first")
'one'
```
