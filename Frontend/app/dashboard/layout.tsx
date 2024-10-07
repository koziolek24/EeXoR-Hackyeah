import NavBar from "@/app/ui/navBar/navBar"
import React from "react";
import Footer from "@/app/ui/footer/footer";

export default function Layout({ children }: Readonly<{
    children: React.ReactNode;
}>) {
    return <><NavBar /><div className="container mt-5 h-75">{children}</div><Footer /></>;
}
