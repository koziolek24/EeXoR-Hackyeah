import type { Metadata } from "next";
import "./globals.scss";
import ImportBootstrap from "@/app/ui/ImportBootstrap";
import React from "react";

export const metadata: Metadata = {
  title: "EduXoR",
  description: "Eduxor app for learning",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <ImportBootstrap />
      <body>
        {children}
      </body>
    </html>
  );
}
