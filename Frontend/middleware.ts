import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'
import { cookies } from "next/headers";
import { login } from "@/app/lib/api/login"
import { verifyLogin } from "@/app/lib/api/verifyLogin";
import { logout } from "@/app/lib/api/logout";


export async function middleware(request: NextRequest) {
    const path = request.nextUrl.pathname;
    let response: NextResponse | undefined;
    if (path === "/login") {
        response = await middlewareForLogin(request);
    } else if (path === "/") {
        response = await middlewareForRoot(request);
    } else if (path.startsWith("/dashboard")) {
        response = await middlewareForDashboard(request);
    }

    return response;
}

async function middlewareForRoot(request: NextRequest) {
    const cookieStore = cookies();
    if(verifyLogin(cookieStore)) {
        return NextResponse.redirect(new URL("/dashboard", request.url));
    }
}

async function middlewareForDashboard(request: NextRequest) {
    const cookieStore = cookies();
    if(!verifyLogin(cookieStore))
    {
        return NextResponse.redirect(new URL('/', request.url));
    }

    if (new URL(request.url).pathname == "/dashboard/logout") {
        const response = NextResponse.redirect(new URL("/", request.url))
        logout(response);
        return response;
    }
}

async function middlewareForLogin(request: NextRequest) {
    let formData;
    try {
        formData = await request.formData();
    } catch (e) {
        console.error(e);
        return NextResponse.redirect(new URL("/", request.url));
    }

    if (request.method !== "POST" || !formData.has("login"))
    {
        return NextResponse.redirect(new URL('/', request.url));
    }

    return login(request.url, formData.get("login")?.toString() as unknown as string);
}

export const config = {
    matcher: [ "/((?!api|static|.*\\..*|_next).*)" ]
};