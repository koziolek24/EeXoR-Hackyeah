import {cookies} from "next/headers";
import {sessionSettings} from "@/middleware";


export default async function Page() {
    const user_id = cookies().get(sessionSettings.cookieName);
    let form = new FormData();
    form.set("user_id", user_id.value);
    const res = await fetch(`${process.env.API_URL}/cf_problems/started/?user_id=${user_id.value}`, {
        method: "POST",
        body: form,
    });
    if (!res.ok) {

    }
    const response = await res.json();
    console.log(response);
    return <h1>solve</h1>;
}