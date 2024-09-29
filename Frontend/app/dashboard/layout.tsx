import NavBar from "@/app/ui/NavBar"
import React from "react";

export default function Layout({ children }: Readonly<{
    children: React.ReactNode;
}>) {
    return <><NavBar />{children}</>;
}
