import { Button } from "@/components/ui/button";
import { TextField } from "./FormComponents";
import Logo from "./Logo";

function Login() {
  return (
    <>
    <Logo />
      <div className=" bg-[#5878d8] h-screen flex p-12">
        <div className="flex-[3] flex items-center justify-center bg-[#96B9F9] rounded-l-md">
          <img className="absolute left-36" src="/images/login.svg" />
        </div>
        <div className="flex-[5] flex flex-col items-center justify-center bg-[#FFFFFF] rounded-r-md">
          <h1 className="font-bold text-2xl">Login</h1>
          <TextField
            id={"email"}
            type={"email"}
            label={"Email"}
            placeholder="Enter your email"
          />
          <TextField
            id={"password"}
            type={"password"}
            label={"Password"}
            placeholder="Enter password"
          />
          <Button className="bg-[#5878d8] my-3 hover:bg-[rgb(64,84,172)] transition-all duration-300 rounded-lg text-black" >Submit</Button>
        </div>
      </div>
    </>
  );
}

export default Login;
