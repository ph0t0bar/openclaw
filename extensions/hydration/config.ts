import { Type, type Static } from "@sinclair/typebox";

export const hydrationConfigSchema = Type.Object({
  // Enable/disable hydration
  enabled: Type.Optional(
    Type.Boolean({
      default: true,
      description: "Enable context hydration",
    })
  ),

  // oPOErator Hub connection
  hubUrl: Type.Optional(
    Type.String({
      default: "https://hub-production-f423.up.railway.app",
      description: "oPOErator Hub URL for fetching drops",
    })
  ),

  apiKey: Type.Optional(
    Type.String({
      description: "API key for oPOErator Hub",
    })
  ),

  userId: Type.Optional(
    Type.String({
      description: "User ID for oPOErator Hub",
    })
  ),

  // Local filesystem paths (optional, in addition to Hub)
  dropPaths: Type.Optional(
    Type.Array(Type.String(), {
      default: [],
      description: "Local directories to scan for drops",
    })
  ),

  checkpointPath: Type.Optional(
    Type.String({
      description: "Directory containing conversation checkpoints",
    })
  ),

  // Limits
  maxDropAge: Type.Optional(
    Type.Number({
      default: 24,
      description: "Maximum age of drops to include (hours)",
    })
  ),

  maxDrops: Type.Optional(
    Type.Number({
      default: 10,
      description: "Maximum number of recent drops to include",
    })
  ),

  cacheTtl: Type.Optional(
    Type.Number({
      default: 60,
      description: "Cache TTL in seconds",
    })
  ),

  // Capture incoming messages as drops (zero AI tokens)
  captureEnabled: Type.Optional(
    Type.Boolean({
      default: false,
      description: "Capture incoming messages as drops (zero AI tokens)",
    })
  ),

  captureChannels: Type.Optional(
    Type.Array(Type.String(), {
      default: [],
      description: "Channels to capture from (empty = all channels)",
    })
  ),
});

export type HydrationConfig = Static<typeof hydrationConfigSchema>;
