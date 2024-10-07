'use client'

import { usePathname } from "next/navigation";
import "@/app/ui/navBar/navBar.scss"
import NavBarElement from "@/app/ui/navBar/navBarElement";


export default function NavBar() {
    const activePath = usePathname();
    return <nav className="navbar navbar-expand-md main-nav navbar-dark">
        <div className="container-fluid">
            <button className="navbar-toggler" type="button" data-bs-toggle="collapse"
                    data-bs-target="#navbar-extended-content" aria-controls="navbar-extended-content"
                    aria-expanded="false" aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbar-extended-content">
                <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                    <NavBarElement path="/dashboard" name="Stats" activePath={activePath} />
                    <NavBarElement path="/dashboard/start-new" name="Start New" activePath={activePath} />
                    <NavBarElement path="/dashboard/solve" name="Solve" activePath={activePath} />
                </ul>
                <ul className="navbar-nav">
                    <NavBarElement path="/dashboard/logout" name="Log Out" activePath={activePath} />
                </ul>
            </div>
        </div>
    </nav>
;
}