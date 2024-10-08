import Logo from "@/app/ui/logo";
import LoginForm from "@/app/ui/loginForm";
import RegisterForm from "@/app/ui/registerForm";


export default function FormContainer({ isRegister = false }) {
    return <main className="vh-100">
        <div className="container py-5 h-100">
            <div className="row d-flex justify-content-center align-items-center h-100">
                <div className="col-12 col-md-8 col-lg-6 col-xl-5">
                    <div className="card bg-dark" style={{borderRadius: '1rem'}}>
                        <div className="card-body px-5 py-2 text-center">
                            <div className="pb-5 mt-4">
                                <h1 className="text-white mb-3"><Logo /></h1>
                                { !isRegister && <LoginForm /> }
                                { isRegister && <RegisterForm /> }
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </main>;
}