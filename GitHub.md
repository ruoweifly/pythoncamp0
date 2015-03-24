#GitHub使用入门教程


##为什么要使用GitHub?
GitHub是为了解决复杂项目和小组写作而生的一家公司/软件。GitHub几乎完美地实现了：

1. 版本控制。像小秘书一样记录你折腾的全过程，追踪你项目的每一个修改。
2. 云盘存储。这样你可以在你的任一电脑/终端上开启项目。
3. 多人合作。可以随便拿别人的项目或生成自己的项目折腾。

换句话说，有了它的帮助，你可以在云端自动储存每一个文件/项目版本，可以放心折腾。理论上，你有无穷大多试验田，放手大胆尝试，也可以邀请别人一起来试验你的项目，并参与到那些你喜欢的项目之中，向牛人学习。


##快速入门GitHub：核心概念
了解一个新事物应该首先了解核心概念，这样才可以快速上手，GitHub中的概念有：

### GitHub中的项目

* `repository`：这是GitHub中的项目概念。你的每一个项目在GitHub中都显示为库。如果你愿意参与别人到项目，可以去`fork`别人的库。
* `issue`：这是GitHub中用来项目跟踪的概念。每一个issue能让你对项目进展有直观认识，而且能引发小组讨论。特别的issue有`milestone`, `lables`,和 `assignees`.
* `wiki`：每个GitHub项目都应该有一个wiki指南，来表达项目中的核心概念，可以让人快速上手。

### GitHub中的项目流（workflow）
参考[Understanding GitHub Workflow][id]

[id]: https://guides.github.com/introduction/flow/

1. branch 分支，每个项目都可以有不同的分支。这样你可以有无限copy，玩命折腾，而不影响到主线。
   * `master` branch：即一个项目的主分支。
   * `fork` projects：你可以从别人那里复制一个项目，自己折腾。如果你对自己的结果满意，可以`pull a request`，完成一次互动。
  
2. add `commits`，项目中毎一个文件的增加，编辑，删除，都在makeing a commit.

3. open a `pull request`: 如果你是从别人那里拷贝了一个库，那么pull request相当于给主人发了一个邀请，如果他们喜欢，他们会接受你的修改。如果你和别人在一起协作一个项目进程，pull request相当于给小组成员发了一个提醒，大家可以一起讨论要不要把这个修改并入`master` branch。
 
4. discuss and review your code。讨论你的修改。
5. merge and depoy。如果对方接受，或者小组成员接受，你可以把你的修改合并到主分支里面。

### 常用命令介绍
入门只需要知道以下几个常用命令，其他推荐查资料。

1. git clone 从远程拷贝到本地。git clone username@host:/path/to/repository

2. 将你的修改推送到GitHub中  
   3个概念：working direcotory(工作区)－－>index（暂存区）－－>head（保存区）－－>GitHub
   
   每一个推送分别使用：
   * git add
   * git commit
   * git push origin master

常用资源：
[git简明指南][id]

[id]: http://rogerdudler.github.io/git-guide/index.zh.html
进阶：[如何高效利用GitHub][id]

[id]:http://www.yangzhiping.com/tech/github.html