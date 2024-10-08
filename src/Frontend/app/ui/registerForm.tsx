import Link from "next/link";
import IncorrectDataPrompt from "@/app/ui/incorrectDataPrompt";


export default function RegisterForm() {
    return <>
        <form action="/register" method="POST">
            <div className="form-floating mb-3">
                <input type="text" name="login" id="login" placeholder="login" className="form-control"/>
                <label htmlFor="login">login</label>
            </div>
            <button className="btn btn-primary btn-large w-100 px-5 py-3" type="submit">
                Register
            </button>
        </form>
        <p className="small mt-3 mb-0 pb-lg-2">
            <Link className="text-white-50" href="/">Log in</Link>
        </p>
        <IncorrectDataPrompt />
    </>;
}