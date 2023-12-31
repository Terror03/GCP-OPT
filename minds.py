import mindspore

num_elements = 64*128*14*14
sequence = mindspore.numpy.arange(0.0001, 0.0001*num_elements + 0.0001, 0.0001,dtype=mindspore.float32)
tensor = sequence.reshape(64, 128, 196)
x = mindspore.Tensor(tensor, mindspore.float32)
num_elements = 64*128*128
sequence = mindspore.numpy.arange(0.0001, 0.0002*num_elements + 0.0001, 0.0002,dtype=mindspore.float32)
tensor = sequence.reshape(64, 128, 128)
input = mindspore.Tensor(tensor, mindspore.float32)
M=196
num_elements = 196*196
sequence = mindspore.numpy.arange(0.0001, 0.0002*num_elements + 0.0001, 0.0002,dtype=mindspore.float32)
tensor = sequence.reshape(196,196)
oo = mindspore.Tensor(tensor, mindspore.float32)
I_hat1 = (-1./196/196)*mindspore.ops.ones((M,M),mindspore.float32) 
I_hat2 =  (1./M)*mindspore.ops.eye(M,M,mindspore.float32)
I_hat1=I_hat1.view(1,M,M).tile((64,1,1))
I_hat2=I_hat2.view(1,M,M).tile((64,1,1))
#print("bmm1")
#print(mindspore.numpy.sum(x.bmm(I_hat1).bmm(x.transpose(0,2,1))))
#print(mindspore.numpy.sum(x.bmm(I_hat1).bmm(x.transpose(0,2,1)))+mindspore.numpy.sum(x.bmm(I_hat2).bmm(x.transpose(0,2,1))))
# print("bmm2")
# print(x.bmm(I_hat2))
# print(I_hat2.bmm(x.transpose(0,2,1)))
# print(x.bmm(I_hat2).bmm(x.transpose(0,2,1)))
# print(mindspore.numpy.sum(x.bmm(I_hat2)))
# print(mindspore.numpy.sum(I_hat2.bmm(x.transpose(0,2,1))))
# print(mindspore.numpy.sum(x.bmm(I_hat2).bmm(x.transpose(0,2,1))))
num_elements = 64*128*128
sequence = mindspore.numpy.arange(0.0001, 0.0001*num_elements + 0.0001, 0.0001,dtype=mindspore.float32)
tensor = sequence.reshape(64, 128, 128)
x1 = mindspore.Tensor(tensor, mindspore.float32)
grad_input = (x1 + x1.transpose(0,2,1)).bmm(x)
#grad_input =grad_input.matmul(I_hat)
print("grad")
print((x1 + x1.transpose(0,2,1)).bmm(x))
print((x1 + x1.transpose(0,2,1)))
print(mindspore.numpy.sum(grad_input))
print("sqrtm")
I3 = mindspore.ops.tile(3.0*mindspore.ops.eye(128,128,x1.dtype).view(1, 128, 128),(64,1,1)).astype(mindspore.float32)


normA = (1.0/3.0)*x1.bmm(I3).sum(axis=1)
print(normA.shape)
normA=normA.sum(axis=1)
print(normA.shape)
print("normA")
print(normA)
normA = (1.0/3.0)*x1.bmm(I3).sum(axis=1).sum(axis=1)
print(normA.shape)
print((1.0/3.0)*x1.bmm(I3))
xxx=(1.0/3.0)*x1.bmm(I3).sum(axis=1)
print(xxx)

print(mindspore.numpy.sum((1.0/3.0)*x1.bmm(I3)))
A = mindspore.ops.div(x1,normA.view(64,1,1).expand_as(x1))
print("A")
print(mindspore.numpy.sum(A))
Y = mindspore.ops.zeros((64, 1, 128, 128),x1.dtype).astype(mindspore.float32)
Z = mindspore.ops.tile(mindspore.ops.eye(128,128,mindspore.float32).view(1,128,128),(64,1,1,1)).astype(mindspore.float32)
if 1 < 2:
    ZY = 0.5*(I3 - A)
    print("ZY")
    print(mindspore.numpy.sum(ZY ))
    YZY = A.bmm(ZY)
    print("YZY")
    print(mindspore.numpy.sum(YZY))
y = YZY*mindspore.ops.sqrt(normA).view(64, 1, 1).expand_as(x1)
print("y")
print(mindspore.numpy.sum(y ))
