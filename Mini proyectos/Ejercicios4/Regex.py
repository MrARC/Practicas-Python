import re

regexNumero = re.compile(r'\d{3}-\d{3}-\d{4}')
regexResult = regexNumero.search('Mi numero es 667-274-9291 y el de ella es 667-742-698')
print(f'Numero encontrado: {regexResult.group()}')

# por grupo
regexNumero = re.compile(r'(\(\d{3}\)) (\d{3}-\d{4})') # igual a = (\(\d\d\d\)) (\d\d\d-\d\d\d\d)
regexResult = regexNumero.search('Mi numero es (415) 555-4242')
print(f'Numero encontrado: {regexResult.group()}')

# con pipas
heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group()) # => evalua a Batman

mo2 = heroRegex.search('Tina Fey and Batman.')
print(mo2.group()) # => evalua a Tina Fey

# grupo y pipas
# esta regex agarra Batman, Batmobile, Batcopter, Batbat
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
batmo = batRegex.search('Batmobile lost a wheel')
print(batmo.group()) #  => Batmobile
print(batmo.group(1)) # => mobile

# match opcional con simbolo ?
batRegex = re.compile(r'Bat(wo)?man') # => podría ser Batman o Batwoman
bo1 = batRegex.search('The adventures of Batman')
print(bo1.group()) # => Batman

bo2 = batRegex.search('The adventures of Batwoman')
print(bo2.group()) # => Batwoman

# hacer opcional el area code

regexNumero = re.compile(r'(\d{3}-)?\d{3}-\d{3}')
rn = regexNumero.search('Mi numero 667-734-9291')
print(rn.group()) # captura todo el num con código de area
rn = regexNumero.search('Mi numero es 744-9291')
print(rn.group()) # captura 744-9291 ya que el código de area es opcional

# si necesitamos hacer match de un signo de interrogación usamos un caracter de escape "\?"