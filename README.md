# Recursive-Create-Folders
To create a serios of folder with a yaml file which is for folder structure

### template of yaml file
```
rootFoler:
    parentFolder1:
        sonFolder1:
            grandsonFolder1:
        sonFolder2:
    parentFolder2:
        sonFolder2:
        sonFolder3:
            grandsonFolder1:
            grandsonFolder2:
```

### example to run
```
./foldergen.py template.yaml 
```

### result based on tempalte yaml file
```
$ tree ./rootFoler
./rootFoler
├── parentFolder1
│   ├── sonFolder1
│   │   └── grandsonFolder1
│   └── sonFolder2
└── parentFolder2
    ├── sonFolder2
    └── sonFolder3
        ├── grandsonFolder1
        └── grandsonFolder2

9 directories, 0 files
```
