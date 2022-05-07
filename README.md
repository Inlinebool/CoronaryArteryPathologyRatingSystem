# CoronaryArteryPathologyRating
A coronary artery pathology rating system based on Syntax scoring system


1.	病变评分的算法主要分为血管分割、三维重建、中心线计算、病变提取和量化四个部分。
2.	血管分割和三维重建由于涉及到交互和图像展示，目前是使用将代码写成开源软件Slicer的插件，利用Slicer的界面进行交互，分割出冠状动脉，并计算出血管中心线。
3.	病变提取和量化代码在 目录 “\冠状动脉病变评分系统\代码\病变计算” 下，该工程需要配置VTK、ITK环境，并将VMTK的库函数导入到项目中。


文件说明：

\冠状动脉病变评分系统\Syntax
介绍Syntax评分的文件

\冠状动脉病变评分系统\代码
\Slicer插件
Slicer插件中分为源代码和编译好的库，Slicer3现在不支持在线安装插件，但可以自己手动安装，需要将动态库放到Slicer指定的插件目录中（默认是C:\Users\Jason\AppData\Local\Temp\Slicer3），重启Slicer后可以在Slicer的Module中可以找到对应模块。
Slicer插件的操作过程见文件“Slicer插件操作.pdf”

\病变计算
病变计算的代码是在VS2008环境下，配置好VTK、ITK环境，并导入VMTK库函数之后通过计算中心线上半径变化的导数等特征提取并量化狭窄病变。
