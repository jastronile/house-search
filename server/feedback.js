const mongoose=require('mongoose');
// mongodb://0.0.0.0:27017/majorDB
mongoose.connect("mongodb+srv://tanishmodase18:projectcluster@cluster0.wbjdiu1.mongodb.net/majorDB?retryWrites=true&w=majority").then(() =>{
    console.log("connected to  FeedbackDB");
}).catch((err)=>{
    console.log(err);
})
const userSchema=mongoose.Schema({
    feedback:String
});

userFeedback= mongoose.model("feedback",userSchema);

module.exports=userFeedback;


