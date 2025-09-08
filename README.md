# 清华大学学生次世代动漫社 社团手册

气泡使用方法：
\chatbubble[left/right]{头像}{昵称}{
这是一段话
}{颜色}
例子：
\chatbubble[right]{zijing.png}{紫荆}{
以下是社员寄语示例。
}{zi}

已经定义了几种颜色：
\definecolor{truepurple}{RGB}{128, 0, 128}  % 主色调紫色
\definecolor{taopink}{HTML}{F17F98}  % 桃子名字
\definecolor{tao}{HTML}{FFF2F9}  % 桃子气泡
\definecolor{zi}{HTML}{F8F2F9}  % 紫荆气泡
\definecolor{qing}{HTML}{F2F9EA}  % 清芬气泡
\definecolor{default}{HTML}{F9F9F9}  %默认气泡灰

一般左侧气泡用default，右侧气泡用zi


图片注释文本框：\picbox{\small ~\ding{115} ~ 图注文字~}
波浪号是空格，可增可删
\ding{115} 是上三角