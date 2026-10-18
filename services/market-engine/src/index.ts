/**
 * FIMAS market-engine scaffold.
 * Exchange rules and equilibrium claims must be specified and tested before use.
 */
export type ResourceOffer = {
  agentId: string;
  quantity: number;
};

export function validateOffer(offer: ResourceOffer): boolean {
  return offer.agentId.trim().length > 0 && Number.isFinite(offer.quantity) && offer.quantity >= 0;
}
