import tenserflow as tf
a = str(2**1000)
alen = len(a)
sum = 0
for x in range(0, alen):
    sum += int(a[x])
print(sum)

b = 0
a = str(10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376)
for x in range(0, len(a)):
    b += int(a[x])
print(b)