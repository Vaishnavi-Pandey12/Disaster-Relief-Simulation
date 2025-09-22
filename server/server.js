import express from 'express';
import { configDotenv } from 'dotenv';

configDotenv()

const app = express();
const PORT = process.env.PORT;

app.get('/api/health',(req,res)=>{
    res.send({
        message: 'api is working perfectly',
        success: true
    });
});

app.listen(PORT, ()=>{
    console.log(`server is running on port: ${PORT}`);
});