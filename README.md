# Simple-file-search
一个简易的文件检索工具 通过python实现

英文需求文档 https://wwi.lanzouw.com/isTJFz40aze

下文为机翻内容

简介

尽管运行个人计算机的操作系统之间存在明显的差异，但是它们都具有一个共同点，那就是文件系统的概念，文件系统的作用是管理文件的创建，排列，更新和删除。诸如硬盘驱动器和USB记忆棒之类的存储设备实际上比看起来复杂得多，但是文件系统提供了这种复杂性的抽象，用一些简单的概念（例如文件，目录和路径）代替了它。 

像许多编程语言库一样，Python的标准库提供了各种文件系统操作的预构建实现。可以创建文件，复制和移动文件，在目录中搜索以及操纵路径。一旦知道了文件系统所围绕的抽象概念，就可以使用Python的标准库以相同的抽象概念访问文件系统。我们已经看到，Python中有一个str类型，它知道如何管理字符序列，而一个float类型，它知道如何存储和处理浮点数。因为它们是Python内置的，所以您可以使用它们而不必知道它们在内部如何工作的每一个细微的细节。类似地，Python标准库提供了诸如Path之类的类型，这些类型可以处理操纵文件系统的细节，这意味着您不必了解它们在内部如何工作的每个细节即可充分利用它们。 

这个项目将使您有机会探索Python标准库的一些以前可能从未见过的部分。提供阅读和摘要技术文档的实践，以确定标准库中哪些功能适合于帮助您解决问题；向您介绍一些以前可能没有机会使用的Python功能，例如异常处理；并要求您使用递归遍历递归数据结构（在这种情况下为文件系统）。 

你会写这个项目该计划是一个可以找到，并在目录中显示所有文件的路径（和潜在的，所有的子目录，及其子目录，等等），然后对某些具有有趣特征的文件采取措施。有趣的角色和采取行动的概念都是可以配置的，并且可以以几种不同的方式工作，但是查找文件的核心行为始终是相同的。您的目标之一是尽可能避免 一遍又一遍地重写相同的代码（例如，多个函数各自执行对特性稍有不同的文件的搜索）；在ICS 32中，我们开始更加严格地关注设计问题，着眼于如何以最佳方式解决程序，而不是编写“可行的”东西。 

您的程序将从控制台以以下格式接收输入。它不应以任何方式提示用户。这里的目的不是要编写一个用户友好的用户界面。您实际上正在做的是构建一个可以自动测试的程序，因此至关重要的是，您的程序必须按以下规定精确地读取输入和写入输出。 


• 首先，程序读取一行输入，该输入指定可以找到哪些文件。可以通过以下两种方式之一进行指定：  o 字母D，后跟一个空格，然后（在该行的其余部分）后面是目录的路径。在这种情况下，将考虑该目录中的所有文件，但不会考虑任何子目录（并且这些子目录中也没有文件）。 （您可以在这里将字母D表示为  
“目录”。） 

o 字母R，后跟一个空格，然后（在该行的其余部分）后面是目录的路径。在这种情况下，将考虑该目录中的所有文件，以及其子目录中的所有文件，其子目录中的所有文件，依此类推。 （您可以在此处将字母R表示为“递归”。） 

o 如果此输入行不遵循此格式，或者指定的目录不存在，请在一行上单独打印ERROR一词，然后重复阅读这行输入；继续直到输入有效。 


• 接下来，程序将打印出正在考虑的每个文件的路径。每个路径都打印在自己的行上，在其之前或之后没有空格，并且每行以换行符结尾。还要注意，文件路径的打印顺序是相关的。您必须按以下顺序打印它们： 

o 首先，打印目录中所有文件的路径。这些文件以文件名的字典顺序打印。 （稍后会按字典顺序提供更多信息，但请注意，这是对字符串进行排序的默认方式。） 

o 接下来，如果考虑了子目录中的文件，则将按照相同的排序规则打印每个子目录中的文件在这里，一个所有文件先于其他子目录中的子目录打印，并且这些子目录按其名称的字母顺序打印。 • 既然程序已经显示了所考虑的每个文件的路径，是时候缩小搜索范围了。程序现在读取输入的一行内容，这些内容描述了搜索特征，这些特征将用于确定文件是否“有趣”并应对其执行操作。有五个不同的特征，此输入行选择其中之一。  

o 如果此输入行仅是一行上的字母A，则认为在上一步中找到的所有文件都很有趣。 

o 如果此输入行以字母N开头，则将搜索名称与特定名称完全匹配的文件。 N后跟一个空格；在空格之后，该行的其余部分将指示要搜索的文件的名称。


▪ 请注意，文件名包含扩展名，因此搜索boo不会找到名为boo.doc的文件。 

o 如果此输入行以字母E开头，则将搜索名称具有特定扩展名的文件。 E后跟一个空格；在空格之后，该行的其余部分将指示所需的扩展名。  


▪ 例如，如果所需的扩展名是py，则所有名称以.py结尾的文件都将被认为是有趣的。所需的扩展名可以在前面加上或不加上点（例如，E .py或E py在输入中表示相同的意思），并且搜索的方式应相同。 


▪ 另外，请注意，名称结尾和扩展名之间会有区别。在我们的程序中，如果搜索正在寻找扩展名为oc的文件，则会找到名为iliveinthe.oc的文件，但不会找到名为invoice.doc的文件。 

o 如果此输入行以字母T开头，则将搜索包含给定文本的文本文件。 T后面将有一个空格；在空格之后，该行的其余部分将指示该文件应包含的文本，以便将其视为有趣的文本。


▪ 例如，如果此输入行在T为True时读为T，则任何包含文本“ while为True”的文本文件都将被认为是有趣的。 


▪ 需要注意的一件事是，并非所有文件都是文本文件，但是您无法通过文件名或扩展名来确定它。可以将其打开并读取为文本文件的任何文件，，视为此处适合我们使用的文本文件

无论其名称如何均被。任何无法打开并不能作为文本文件读取的文件都应跳过（即，它不被认为是有趣的）。 

o 如果此输入行以字符<开头，则搜索将查找其大小（以字节为单位）小于指定阈值的文件。 <后跟一个空格；在空格之后，其余行将是一个非负整数值，用于指定大小阈值。 


▪ 例如，输入<65536意味着大小不超过65,535字节（即，小于65,536字节）的文件将被认为是有趣的。 

o 如果此输入行以字符>开头，则将搜索其大小（以字节为单位）大于指定阈值的文件。 >后跟一个空格；在空格之后，其余行将是一个非负整数值，用于指定大小阈值。  


▪ 例如，输入> 2097151意味着大小至少为2,097,152字节（即，大于2,097,151字节）的文件将被认为是有趣的。 

o 如果此输入行与上述格式之一不匹配，请在一行上单独打印ERROR一词，然后重复读取输入行；否则，请重新输入该行。继续直到输入有效。请注意，指定不匹配文件的搜索特征不是错误。仅当此输入行在结构上无效时（即，它与上述格式之一不匹配），这只是一个错误。 


• 接下来，程序将基于搜索特征将路径打印到每个被认为有趣的文件。每个路径都打印在自己的行上，在其之前或之后没有空格，并且每行以换行符结尾。应该使用与上次打印时相同的排序规则（即，按字典顺序排序）来打印路径，但是，当然，这次您可能会打印较少的内容，因为并非每个文件都必须符合搜索条件特征。


• 如果没有有趣的文件，则程序结束；否则，程序结束。没有采取任何行动。 


• 现在我们缩小了搜索范围，是时候对找到的文件采取行动了。将按照与先前打印文件相同的顺序对文件执行操作。程序现在读取一行输入，该输入描述将对每个有趣的文件执行的操作。有三种不同的操作，此输入行选择其中之一。 

o 如果输入的这一行本身包含字母F，则如果是文本文件，则从文件中打印文本的第一行；否则，请从文件的第一行开始打印。如果不是，则打印NOT TEXT。 8

o 如果此输入行本身包含字母D，请复制该文件并将其存储在原始文件所在的目录中，但是该副本应在文件名后附加.dup（“ duplicate”的缩写）。 。例如，如果有趣的文件是C：\ pictures \ boo.jpg，则可以将其复制到C：\ pictures \ boo.jpg.dup。 

o 如果输入的第三行本身包含字母T，则“触摸”文件，这意味着将其最后修改的时间戳修改为当前日期/时间。 

o 如果此输入行与上述格式之一不匹配，请在一行上单独打印ERROR一词，然后重复读取输入行；否则，请重新输入该行。继续直到输入有效。


• 对每个文件采取措施后，程序结束。一些附加说明 
由于此项目的目标之一是向您介绍使用递归解决实际问题的方法，因此，包含子目录及其子目录的搜索必须实现为递归Python函数，该函数可以处理一个子目录中的所有文件。目录，然后递归处理所有子目录。 （请注意，这排除了Python标准库的某些功能-此类搜索实际上已内置在该库中，但会绕过此处的学习目标。稍后将进一步介绍。） 

除了出现符号链接外，我们忽略此项目的目的，目录结构是分层的（即目录内部有子目录，而这些子目录与“父目录”具有相同的基本结构）。 

程序执行程序执行的示例以下是的示例，因为完成后它应该可以工作。粗体斜体文本表示输入，而普通文本表示输出。所示的目录和文件是假设的，但如上所述，说明了输入和输出的结构。 
为了重申之前的观点，您的程序不应以任何方式提示用户。假定用户知道要使用的正确格式，它应该读取输入。


R C:\Test\Project1\Example

C:\Test\Project1\Example\test1.txt

C:\Test\Project1\Example\test2.txt

C:\Test\Project1\Example\Sub\meee.txt

C:\Test\Project1\Example\Sub\test1.txt

C:\Test\Project1\Example\Sub\youu.txt

C:\Test\Project1\Example\Zzz\zzz.py

N

ERROR

N test1.txt

C:\Test\Project1\Example\test1.txt

C:\Test\Project1\Example\Sub\test1.txt

Q

ERROR

F

This is a line of text

Hello, my name is Boo

