# CSE7024_Project
Implementation of BC backed DL  
Much work left to be done  
Everything but the datasets are to be included in the data section of a block. The model container allows information to be included that is not actually part of the model parameters, such as discussions or notes about the model.  
The most challengeing part of the implementation is figuring out how to evaluate models. If external frameworks, such as PyTorch or TensorFlow are used, how to run the training from the chain?  
'9linenn.py' is example to copy-paste the contents to show a model can be added and run  
#--TODO--    
- [x] implement adding a model to a block  
- [x] evaluate a model  
- [x] compare to existing best model  
- [x] sign model    
- [x] implement broadcasting and beaconing  
- [x] add methods to save/load blockchain to/from nonvolatile storage
- [ ] develop means to check acceptance level to determine whether or not block gets added to chain  
- [ ] implement means to check if model is compatible with device  
