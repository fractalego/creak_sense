# Testing whether a sentence is consistent with the CREAK dataset
This framework is trained on the [CREAK dataset](https://arxiv.org/abs/2109.01653).


# Install
pip install creak-sense


# Example 
```python

from creak_sense import CreakSense

sense = CreakSense("fractalego/creak-sense")

claim = "Bananas can be found in a grocery list"
sense.make_sense(claim)
```
with output "True".


# Example with explanation 
```python

from creak_sense import CreakSense

sense = CreakSense("fractalego/creak-sense")

claim = "Bananas can be found in a grocery list"
sense.get_reason(claim)
```
with output "Bananas are a staple food".
