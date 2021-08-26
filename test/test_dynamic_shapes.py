# Run:
# XLA_EXPERIMENTAL="nonzero:masked_select" python3 <test_dynamic_shapes.py>
#

import torch
import torch_xla

class TestDynamicShapes(object):
  def __init__(self):
    self.device = 'xla:0'
  def runTest(self):
    t1 = torch.tensor([1,0,2,0,0,1,3], device=self.device)
    
    t2 = torch.nonzero(t1)
    t2_dim0_shape = torch_xla._XLAC._get_xla_tensor_dimension_size(t2, 0)
    print(t2_dim0_shape)
    print(torch_xla._XLAC._get_xla_tensors_text([t2]))
    print(torch_xla._XLAC._get_xla_tensors_hlo([t2]))
    self.assertEqual(t2_dim0_shape.item(), 4)
    
    t3 = torch.fill_(t2, 10)
    t2_dim0_shape = torch_xla._XLAC._get_xla_tensor_dimension_size(t2, 0)
    t3_dim0_shape = torch_xla._XLAC._get_xla_tensor_dimension_size(t3, 0)
    print(torch_xla._XLAC._get_xla_tensor_dimension_size(t2, 0))
    print(torch_xla._XLAC._get_xla_tensor_dimension_size(t3), 0)
    print(torch_xla._XLAC._get_xla_tensors_hlo([t2]))
    print(torch_xla._XLAC._get_xla_tensors_hlo([t3]))
    print(torch_xla._XLAC._get_xla_tensors_text([t2]))
    print(torch_xla._XLAC._get_xla_tensors_text([t3]))
    self.assertEqual(t2_dim0_shape.item(), 4)
    self.assertEqual(t3_dim0_shape.item(), 4)
    
if __name__ == "__main__":
  test = TestDynamicShapes()
  test.runTest()