# CSE7024_Project
Implementation of BC backed DL  
Much work left to be done  
Everything but the datasets are to be included in the data section of a block. The model container allows information to be included that is not actually part of the model parameters, such as discussions or notes about the model.  
The most challengeing part of the implementation is figuring out how to evaluate models. If external frameworks, such as PyTorch or TensorFlow are used, how to run the training from the chain?  
It might be better to have only one model per block
'9linenn.py' is example to copy-paste the contents to show a model can be added and run  
#--TODO--    
:heavy_check_mark: implement adding a model to a block  
:heavy_check_mark: evaluate a model  
:heavy_check_mark: compare to existing best model  
:heavy_check_mark: sign model    
:white_check_mark: implement broadcasting and beaconing  
:heavy_check_mark: add methods to save/load blockchain to/from nonvolatile storage
- [ ] develop means to check acceptance level to determine whether or not block gets added to chain  
- [ ] implement means to check if model is compatible with device  

