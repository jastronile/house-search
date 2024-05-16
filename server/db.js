const mongoose=require('mongoose');
// mongodb://0.0.0.0:27017/majorDB
mongoose.connect("mongodb+srv://tanishmodase18:projectcluster@cluster0.wbjdiu1.mongodb.net/majorDB?retryWrites=true&w=majority").then(() =>{
    console.log("connected to mongoDB");
}).catch((err)=>{
    console.log(err);
})
const userSchema=mongoose.Schema({
    name:String,
    city:String,
    gender:String,
    age:Number,
    occupation:String,
    budget:Number,
    area:String,
    preference:String
});

user= mongoose.model("user",userSchema);

module.exports=user;


