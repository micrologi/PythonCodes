nums = [float(iCont) for iCont in input('Digite nºs: ').split()]

soma = 0
for iCont in range(len(nums)):
   soma += nums[iCont]
   
print(f'{soma}')
