import "@/app/ui/navBar/navBar.scss"
import Link from "next/link";


export default function NavBarElement({ path, name, activePath }: { path: string; name: string, activePath: string }) {
    const linkClassesName = activePath === path ? "active nav-link" : "nav-link";
    return <li className="navbar-item">
        <Link href={ path } className={linkClassesName} >{ name }</Link>
    </li>;
}