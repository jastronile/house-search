const mongoose=require('mongoose');
// mongodb://0.0.0.0:27017/majorDB
mongoose.connect("mongodb+srv://tanishmodase18:projectcluster@cluster0.wbjdiu1.mongodb.net/majorDB?retryWrites=true&w=majority").then(() =>{
    console.log("connected to amentiesmongoDB");
}).catch((err)=>{
    console.log(err);
})
const userSchema=mongoose.Schema({
    Latitude:Number,
    Longitude:Number,
});

required_amenities= mongoose.model("required_amenitie",userSchema);

module.exports=required_amenities;


