"use client";

import ThemeToggle from "./ThemeToggle";
import { HiOutlineMenu } from "react-icons/hi";
import Link from "next/link";

export default function Navbar() {
  const pages = [
    {
      title: "Leagues",
      href: "/leagues",
    },
    {
      title: "Players",
      href: "/players",
    },
  ];
  return (
    <div className="navbar bg-base-100">
      <div className="navbar-start">
        <div className="dropdown">
          <div tabIndex={0} role="button" className="btn btn-ghost lg:hidden">
            <HiOutlineMenu /> {/* Burger icon */}
          </div>
          <ul
            tabIndex={0}
            className="menu menu-sm dropdown-content bg-base-100 rounded-box z-[1] mt-3 w-52 p-2 shadow"
          >
            {pages.map((page) => (
              <Link key={page.title} href={page.href}>
                {page.title}
              </Link>
            ))}
          </ul>
        </div>
        <Link key="home" href="/" className="text-xl">
          FootPie
        </Link>
      </div>
      <div className="navbar-center hidden lg:flex">
        <ul className="menu menu-horizontal px-1">
          {pages.map((page) => (
            <Link className="px-1 text-xl" key={page.title} href={page.href}>
              {page.title}
            </Link>
          ))}
        </ul>
      </div>
      <div className="navbar-end">
        <ThemeToggle />
      </div>
    </div>
  );
}
