import NavBar from "@/app/ui/navBar/navBar"
import React from "react";

export default function Layout({ children }: Readonly<{
    children: React.ReactNode;
}>) {
    return <><NavBar />{children}</>;
}
