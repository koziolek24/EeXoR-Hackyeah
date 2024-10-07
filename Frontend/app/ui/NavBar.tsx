import "@/app/ui/NavBar.scss"
import Link from "next/link";


export default function NavBar() {
    return <nav className="navbar navbar-expand-md main-nav navbar-dark">
        <div className="container-fluid">
            <button className="navbar-toggler" type="button" data-bs-toggle="collapse"
                    data-bs-target="#navbar-extended-content" aria-controls="navbar-extended-content"
                    aria-expanded="false" aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbar-extended-content">
                <ul className="navbar-nav">
                    <li className="navbar-item"><Link className="nav-link" href="/dashboard">stats</Link></li>
                    <li className="navbar-item"><Link className="nav-link" href="/dashboard/start-new">start new</Link></li>
                    <li className="navbar-item"><Link className="nav-link" href="/dashboard/solve">solve</Link></li>
                    <li className="navbar-item"><Link className="nav-link" href="/dashboard/logout">log out</Link></li>
                </ul>
            </div>
        </div>
    </nav>
;
}