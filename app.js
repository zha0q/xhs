//导入express模块
const express = require('express');
//创建实例
const app = express();
//创建路由
const router = express.Router();

const { execSync } = require('child_process');

//挂载到app
app.use('/api', router);
//编写接口
router.post('/notes/search', (req, res) => {
    console.log(123);
    const path = `${process.cwd()}/example/my_test.py`;
    console.log('🚀 ~ router.post ~ path:', path);
    const data = execSync(`python ${path}`);
    console.log('🚀 ~ router.post ~ data:', data.toString());
    return res.send({ status: 200, message: '查询成功', data: data.toString() });
});
//建立服务器
app.listen(8123, () => {
    console.log('server running at http://127.0.0.1:8123');
});
