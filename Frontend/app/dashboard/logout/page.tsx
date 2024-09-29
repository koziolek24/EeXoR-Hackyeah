import { redirect } from "next/navigation";



export default async function LogoutPage() {
'use server';
    redirect("/");
}