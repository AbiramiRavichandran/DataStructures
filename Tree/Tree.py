class TreeNode:
  def __init__(self, name ,designation):
      self.name = name
      self.designation = designation
      self.parent = None
      self.children = []

  def addChild(self,child):
      self.children.append(child)
      child.parent = self


def buildTree():
    root = TreeNode("Nilupul", "CEO")

    cto = TreeNode("Chinmay","CTO")
    hrHead = TreeNode("Geels","HR Head")

    InfrastructureHead = TreeNode("Viswa","Infrastructure Head")
    InfrastructureHead.addchild(TreeNode("Dhaval","Cloud Manager"))
    InfrastructureHead.addchild(TreeNode("Abijith","App Manager"))

    cto.addChild(InfrastructureHead)
    cto.addChild(TreeNode("Aamir","Application Head"))

    hrHead.addChild(TreeNode("Peter","Recruitment Manager"))
    hrHead.addChild(TreeNode("Waqas","Policy Manager"))

    root.addChild(cto)
    root.addChild(hrHead)

    return root


    pass


if __name__ == "__main__":
    root = buildTree()
