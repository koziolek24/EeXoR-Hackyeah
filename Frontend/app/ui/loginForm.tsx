import IncorrectDataPrompt from "@/app/ui/incorrectDataPrompt";
import Link from "next/link";


export default function LoginForm() {
    return <>
            <form action="/login" method="POST">
                <div className="form-floating mb-3">
                    <input type="text" name="login" id="login" placeholder="login" className="form-control"/>
                    <label htmlFor="login">login</label>
                </div>
                <button className="btn btn-primary btn-large w-100 px-5 py-3" type="submit">
                    Log in
                </button>
            </form>
            <p className="small mt-3 mb-0 pb-lg-2">
                <Link className="text-white-50" href="/register">Register</Link>
            </p>
            <IncorrectDataPrompt message="Please enter valid login!" />
    </>;
}