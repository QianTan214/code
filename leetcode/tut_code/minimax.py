"""对抗搜索"""


Some important notes as well: 
1) only in a Max node can update the corresponding alpha, so does Min for beta.
2) alpha and beta can only be passed down from its parent


alpha: max节点当前得到的最高收益
beta：min节点当前可给对手的最小收益

alpha, beta初始值 -inf 和 inf

每个节点有两个值alpha 和 beta
如果一个节点中 alpha 大于 beta，则这个节点将被剪枝prunning
