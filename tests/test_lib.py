from x2cdict.lib import gen_dictname 

def test_gen_dictname():
  name = gen_dictname("es", "cn")
  assert name == "es2cn"
  name = gen_dictname("en", "cn")
  assert name == "en2cn"
