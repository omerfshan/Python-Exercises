class Comment:
    def __init__(self,username,text,likes,dislikes):
        self.username=username
        self.text=text
        self.likes=likes
        self.dislikes=dislikes

c1=Comment("hakan","crazy",True,False)
CommentList=[c1]
for c in CommentList:
    print(f"{c.username} {c.text} {c.likes} {c.dislikes}")
        