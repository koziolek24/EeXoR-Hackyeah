import Logo from "@/app/ui/logo";


export default function Footer() {
    return  <div className="container-fluid main-footer bg-black text-white mt-auto">
                <div className="container">
                    <footer className="py-3 my-4 text-center">
                        <p><Logo /> by <Logo EduXor={false} />.</p>
                        <p> Copyright 2024 &copy; Marek Dzięcioł, Maciej Kozłowski, Jakub Mieczkowski, Mateusz Wawrzyniak. All rights reserved.</p>
                    </footer>
                </div>
            </div>;
}