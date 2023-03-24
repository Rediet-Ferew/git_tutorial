import pytest
from arthimetics import Athimetic_Operations

class Arthimetic_Test:
    def test_add(self):
        # arrange
        x, y = 1.0, 2.0
        add_expected_output = 3.0
        sub_expected_output = -1.0
        mul_expected_output = 6.0
        div_expected_output = 6.0
        # act
        add_actual_output= ArthimeticClass.add(x, y)
        sub_actual_output= ArthimeticClass.subtract(x, y)
        mul_actual_output= ArthimeticClass.multiply(x, y)
        div_actual_output= ArthimeticClass.divide(x, y)
        
        #assert
        #test for addition
        with pytest.raises(TypeError):
            ArthimeticClass.add("1", 2)
        with pytest.raises(TypeError):
            ArthimeticClass.add(1, "2")
        with pytest.raises(TypeError):
            ArthimeticClass.add("1", "2")
        #test for subtraction
        with pytest.raises(TypeError):
            ArthimeticClass.subtract("1", 2)
        with pytest.raises(TypeError):
            ArthimeticClass.subtract(1, "2")
        with pytest.raises(TypeError):
            ArthimeticClass.subtract("1", "2")
            
        #test for multiplication
        with pytest.raises(TypeError):
            ArthimeticClass.multiply("1", 2)
        with pytest.raises(TypeError):
            ArthimeticClass.multiply(1, "2")
        with pytest.raises(TypeError):
            ArthimeticClass.multiply("1", "2")
            
        # test for division
        with pytest.raises(TypeError):
            ArthimeticClass.divide("1", 2)
        with pytest.raises(TypeError):
            ArthimeticClass.divide(1, "2")
        with pytest.raises(TypeError):
            ArthimeticClass.divide("1", "2")
        # test for zero division error 
        with pytest.raises(TypeError):
            ArthimeticClass.divide(2, 0)
             
            
        assert add_expected_output == add_actual_output
        assert sub_expected_output == sub_actual_output
        assert mul_expected_output == mul_actual_output
        assert div_expected_output == div_actual_output
        