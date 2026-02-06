import { describe, expect, it } from "vitest";
import { isTrustedProxyAddress, resolveGatewayListenHosts } from "./net.js";

describe("isTrustedProxyAddress", () => {
  it("matches exact IP", () => {
    expect(isTrustedProxyAddress("10.0.0.1", ["10.0.0.1"])).toBe(true);
  });

  it("rejects non-matching exact IP", () => {
    expect(isTrustedProxyAddress("10.0.0.2", ["10.0.0.1"])).toBe(false);
  });

  it("matches CIDR /8 range", () => {
    expect(isTrustedProxyAddress("10.1.2.3", ["10.0.0.0/8"])).toBe(true);
    expect(isTrustedProxyAddress("10.255.255.255", ["10.0.0.0/8"])).toBe(true);
    expect(isTrustedProxyAddress("11.0.0.1", ["10.0.0.0/8"])).toBe(false);
  });

  it("matches CIDR /12 range (Docker-style)", () => {
    expect(isTrustedProxyAddress("172.17.0.1", ["172.16.0.0/12"])).toBe(true);
    expect(isTrustedProxyAddress("172.31.255.255", ["172.16.0.0/12"])).toBe(true);
    expect(isTrustedProxyAddress("172.32.0.1", ["172.16.0.0/12"])).toBe(false);
  });

  it("matches CIDR /10 range (CGNAT/Tailscale)", () => {
    expect(isTrustedProxyAddress("100.64.0.1", ["100.64.0.0/10"])).toBe(true);
    expect(isTrustedProxyAddress("100.127.255.255", ["100.64.0.0/10"])).toBe(true);
    expect(isTrustedProxyAddress("100.128.0.1", ["100.64.0.0/10"])).toBe(false);
  });

  it("matches /32 as exact match", () => {
    expect(isTrustedProxyAddress("192.168.1.1", ["192.168.1.1/32"])).toBe(true);
    expect(isTrustedProxyAddress("192.168.1.2", ["192.168.1.1/32"])).toBe(false);
  });

  it("matches /0 as match-all", () => {
    expect(isTrustedProxyAddress("1.2.3.4", ["0.0.0.0/0"])).toBe(true);
  });

  it("handles ::ffff:-mapped IPv4", () => {
    expect(isTrustedProxyAddress("::ffff:172.17.0.1", ["172.16.0.0/12"])).toBe(true);
  });

  it("returns false for undefined/empty inputs", () => {
    expect(isTrustedProxyAddress(undefined, ["10.0.0.0/8"])).toBe(false);
    expect(isTrustedProxyAddress("10.0.0.1", [])).toBe(false);
    expect(isTrustedProxyAddress("10.0.0.1", undefined)).toBe(false);
  });

  it("checks multiple entries (exact + CIDR)", () => {
    expect(isTrustedProxyAddress("192.168.1.1", ["10.0.0.0/8", "192.168.1.1"])).toBe(true);
    expect(isTrustedProxyAddress("10.5.5.5", ["10.0.0.0/8", "192.168.1.1"])).toBe(true);
    expect(isTrustedProxyAddress("8.8.8.8", ["10.0.0.0/8", "192.168.1.1"])).toBe(false);
  });
});

describe("resolveGatewayListenHosts", () => {
  it("returns the input host when not loopback", async () => {
    const hosts = await resolveGatewayListenHosts("0.0.0.0", {
      canBindToHost: async () => {
        throw new Error("should not be called");
      },
    });
    expect(hosts).toEqual(["0.0.0.0"]);
  });

  it("adds ::1 when IPv6 loopback is available", async () => {
    const hosts = await resolveGatewayListenHosts("127.0.0.1", {
      canBindToHost: async () => true,
    });
    expect(hosts).toEqual(["127.0.0.1", "::1"]);
  });

  it("keeps only IPv4 loopback when IPv6 is unavailable", async () => {
    const hosts = await resolveGatewayListenHosts("127.0.0.1", {
      canBindToHost: async () => false,
    });
    expect(hosts).toEqual(["127.0.0.1"]);
  });
});
