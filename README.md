# Folder-Tree-Generator

## Description
Creates folder tree/structure  

**Modules**  :  `math`, `os`

**Range** 
* number of levels is limited by the max size of a list, which is 536870912
* number of folders in each level is limited by the maximum size of the list, which is 536870912

## Useage

1. **First Example**

```
 Enter folder structure : 1_12

 Your structure is correct

 Enter a name of 1 level : alfa

 Enter a name of 2 level : beta


   	    └───alfa_1
    		├───beta_1
    		├───beta_2
    		├───beta_3
    		├───beta_4
    		├───beta_5
    		├───beta_6
    		├───beta_7
    		├───beta_8
    		├───beta_9
    		├───beta_10
    		├───beta_11
    		└───beta_12
```

2. **Second Example**

```
 Enter folder structure : 1_2_2_2_2

 Your structure is correct

 Enter a name of 1 level : alfa
 Enter a name of 2 level : beta
 Enter a name of 3 level : gamma
 Enter a name of 4 level : fi
 Enter a name of 5 level : theta


alfa_1
    ├───beta_1
    │   ├───gamma_1
    │   │   ├───fi_1
    │   │   │   ├───theta_1
    │   │   │   └───theta_2
    │   │   └───fi_2
    │   │       ├───theta_1
    │   │       └───theta_2
    │   └───gamma_2
    │       ├───fi_1
    │       │   ├───theta_1
    │       │   └───theta_2
    │       └───fi_2
    │           ├───theta_1
    │           └───theta_2
    └───beta_2
        ├───gamma_1
        │   ├───fi_1
        │   │   ├───theta_1
        │   │   └───theta_2
        │   └───fi_2
        │       ├───theta_1
        │       └───theta_2
        └───gamma_2
            ├───fi_1
            │   ├───theta_1
            │   └───theta_2
            └───fi_2
                ├───theta_1
                └───theta_2
```
